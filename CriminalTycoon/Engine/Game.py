class Game:
    def __init__(self, player_name):
        self.day = 0
        self.player_name = player_name
        self.available_mission_list = []
        self.available_criminal_list = []
        self.player_owned_criminal_list = []
        self.current_safe_house = None  # TODO will be safehouse object
        self.available_safe_house_list = []
        self.mission_tracker = []
        self.previous_day_report = None

    def next_day(self):
        # go through each mission and execute it
        for i in range(len(self.mission_list)):
            pass  # probably use a day_report = mission.execute  type thing

        # go to next day
        self.day += 1

    def execute_mission(self):
        pass  # pass/fail mission

    def previous_day_report(self):
        return self.previous_day_report  # return the status report

    def info_character(self):
        return self.player_name  # will want to return more info later, but this works

    def view_available_missions(self):  # go through all player's criminal
        return self.available_mission_list

    def info_mission(self, mission_id):
        self.available_mission_list.index(mission_id)

    def set_mission(self, char, mission_id, cut):
        pass  # stuff goes here

    def view_available_criminal(self):
        pass

    def info_available_criminal(self, criminal_id):
        pass

    def offer_job_to_criminal(self, criminal_id):
        pass



