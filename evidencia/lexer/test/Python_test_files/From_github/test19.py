import random

class Athlete:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.medals = {"Gold": 0, "Silver": 0, "Bronze": 0}

    def win_medal(self, medal_type):
        self.medals[medal_type] += 1

    def get_total_medals(self):
        return sum(self.medals.values())

class Event:
    def __init__(self, name, participants):
        self.name = name
        self.participants = participants

    def conduct_event(self):
        # Simulate the event and determine winners
        gold_winner = random.choice(self.participants)
        silver_winner = random.choice([athlete for athlete in self.participants if athlete != gold_winner])
        bronze_winner = random.choice([athlete for athlete in self.participants if athlete != gold_winner and athlete != silver_winner])

        # Award medals to winners
        gold_winner.win_medal("Gold")
        silver_winner.win_medal("Silver")
        bronze_winner.win_medal("Bronze")

    def display_results(self):
        print(f"\n{self.name} Results:")
        print("----------------------")
        for i, athlete in enumerate(self.participants, start=1):
            print(f"{i}. {athlete.name} ({athlete.country}) - Gold: {athlete.medals['Gold']}, Silver: {athlete.medals['Silver']}, Bronze: {athlete.medals['Bronze']}")
        print("----------------------")

class OlympicGames:
    def __init__(self, events, countries):
        self.events = events
        self.countries = countries

    def conduct_olympics(self):
        print("Welcome to the Olympic Games!")
        print("-----------------------------")

        for event in self.events:
            print(f"\n{event.name} is starting...")
            event.conduct_event()
            event.display_results()

        print("\nOlympic Games concluded!")
        print("------------------------")

        overall_medal_table = self.generate_overall_medal_table()
        print("\nOverall Medal Table:")
        print("-------------------")
        for i, country in enumerate(overall_medal_table, start=1):
            total_medals = sum(country.values())
            gold_medals = country["Gold"]
            silver_medals = country["Silver"]
            bronze_medals = country["Bronze"]
            print(f"{i}. {country['Name']} - Gold: {gold_medals}, Silver: {silver_medals}, Bronze: {bronze_medals} (Total: {total_medals})")
        print("-------------------")

    def generate_overall_medal_table(self):
        medal_table = {}
        for country in self.countries:
            country_medals = {"Name": country, "Gold": 0, "Silver": 0, "Bronze": 0}
            for event in self.events:
                for athlete in event.participants:
                    if athlete.country == country:
                        country_medals["Gold"] += athlete.medals["Gold"]
                        country_medals["Silver"] += athlete.medals["Silver"]
                        country_medals["Bronze"] += athlete.medals["Bronze"]
            medal_table[country] = country_medals
        sorted_medal_table = sorted(medal_table.items(), key=lambda x: sum(x[1].values()), reverse=True)
        return [medal[1] for medal in sorted_medal_table]

# Define athletes
athlete1 = Athlete("John Doe", "USA")
athlete2 = Athlete("Jane Smith", "USA")
athlete3 = Athlete("David Johnson", "Canada")
athlete4 = Athlete("Emma Wilson", "Canada")
athlete5 = Athlete("Michael Brown", "Great Britain")
athlete6 = Athlete("Sophia Anderson", "Great Britain")

# Define events
event1 = Event("100m Sprint", [athlete1, athlete2, athlete3, athlete4, athlete5, athlete6])
event2 = Event("Long Jump", [athlete1, athlete2, athlete3, athlete4, athlete5, athlete6])
event3 = Event("Swimming", [athlete1, athlete2, athlete3, athlete4, athlete5, athlete6])

# Define Olympic Games
olympics = OlympicGames([event1, event2, event3], ["USA", "Canada", "Great Britain"])

# Conduct and display the results of the Olympic Games
olympics.conduct_olympics()
