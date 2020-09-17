from bs4 import BeautifulSoup
import requests
import re

# My personal keys for testing the API
try:
    import testkeys
except ImportError:
    pass # super dumb but i need it for debugging atm

class AuthFailure(Exception):
    """In case API authentication fails"""
    pass


class SchoolSoft(object):
    """SchoolSoft Core API (Unofficial)"""

    def __init__(self, school = "nti", username = "Malte.lindeneveling", password = "qweasd123", usertype = 1):
        """
        school = School being accessed
        username = Username of account being logged in
        password = Password of account being logged in
        usertype = Type of account;
        0 = teacher, 1 = student
        """
        self.school = school

        self.username = username
        self.password = password
        self.usertype = usertype

        self.cookies = {}

        _login_page_re = r"https://sms.schoolsoft.se/nti/html/redirect_login.htm"
        self._login_page_re = re.compile(_login_page_re)

        # Might not be needed, still gonna leave it here
        self.login_page = "https://sms.schoolsoft.se/{}/jsp/Login.jsp".format(school)

    def try_get(self, url, attempts = 0):
        """
        Tries to get URL info using
        self.username && self.password

        Mainly for internal calling;
        however can be used to fetch from pages not yet added to API.
        """
        r = requests.get(url, cookies=self.cookies)

        login_page_match = self._login_page_re.match(r.url)
        if login_page_match:
            server_n = login_page_match.groups()
            if attempts < 1:
                # Sends a post request with self.username && self.password
                loginr = requests.post(self.login_page, data = {
                    "action": "login",
                    "usertype": self.usertype,
                    "username": self.username,
                    "password": self.password
                    }, cookies=self.cookies, allow_redirects=False)

                # Saves login cookie for faster access after first call
                self.cookies = loginr.cookies

                return self.try_get(url, attempts+1)
            else:
                raise AuthFailure("Invalid username or password")
        else:
            return r


    def fetch_schedule(self):
        """
        Fetches the schedule of logged in user
        Returns an (not currently) ordered list with days going from index 0-4
        This list contains all events on that day
        """
        #TODO: Make sure the list is in order

        schedule_html = self.try_get("https://sms.schoolsoft.se/{}/jsp/student/right_student_schedule.jsp?menu=schedule".format(self.school))
        schedule = BeautifulSoup(schedule_html.text, "html.parser")

        full_schedule = []

        for a in schedule.find_all("a", {"class": "schedule"}):
            info = a.find("span")
            info_pretty = info.get_text(separator=u"<br/>").split(u"<br/>")
            full_schedule.append(info_pretty)

        return full_schedule



# Testing shit, uses my testkeys
api = SchoolSoft(testkeys.school, testkeys.username, testkeys.password)

# Example calls
schedule = api.fetch_schedule()
