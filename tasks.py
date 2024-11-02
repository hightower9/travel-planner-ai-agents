from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a 7-Day Travel Itinerary
            **Description**: Expand the city guide into a full 7-day travel itinerary with detailed 
                per-day plans, including weather forecasts, places to eat, packing suggestions, 
                and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay, 
                and actual restaurants to go to. This itinerary should cover all aspects of the trip, 
                from arrival to departure, integrating the city guide information with practical travel logistics.

            **Parameters**: 
            - City: {city}
            - Trip Date: {travel_dates}
            - Traveler Interests: {interests}

            **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent(
                """
                **Expected Output**:
                - A detailed 7-day itinerary for {city} that includes:
                - **Daily Breakdown**: Each day should include at least three major activities (e.g., attractions, experiences) with brief descriptions.
                - **Weather Forecast**: Include daily weather forecast details if available, or typical weather conditions for the given season.
                - **Dining Suggestions**: At least two restaurant recommendations per day, tailored to traveler interests.
                - **Accommodation**: Recommendations for hotels or places to stay, with options for different budget levels (e.g., budget, mid-range, luxury).
                - **Packing Suggestions**: List of essential items to bring based on the weather and planned activities.
                - **Budget Breakdown**: An approximate daily budget for accommodation, meals, activities, and transportation, in the currency of the destination.
                """
            ),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Identify the Best City for the Trip
                    **Description**: Analyze and select the best city for the trip based on specific 
                        criteria such as weather patterns, seasonal events, and travel costs. 
                        This task involves comparing multiple cities, considering factors like current weather 
                        conditions, upcoming cultural or seasonal events, and overall travel expenses. 
                        Your final answer must be a detailed report on the chosen city, 
                        including actual flight costs, weather forecast, and attractions.


                    **Parameters**: 
                    - Origin: {origin}
                    - Cities: {cities}
                    - Interests: {interests}
                    - Travel Date: {travel_dates}

                    **Note**: {self.__tip_section()}
        """
            ),
            expected_output = dedent(
                """
                **Expected Output**:
                - A comprehensive report on the selected city that includes:
                - **Chosen City**: Name of the selected city that best matches the criteria.
                - **Weather Forecast**: A summary of the expected weather during the travel dates, highlighting temperature ranges and conditions (e.g., sunny, rainy).
                - **Seasonal Events**: A list of any major cultural or seasonal events taking place in the city during the travel dates.
                - **Travel Costs**:
                    - **Flight Costs**: Average or lowest available round-trip flight cost from {origin} to the selected city.
                    - **Accommodation Costs**: Estimated daily accommodation rates with options for different budget levels.
                - **Top Attractions**: A list of must-visit attractions or activities that align with traveler interests.
                - **Comparison Summary**: A brief overview of why this city was selected over the others, including key factors like better weather, relevant events, or favorable costs.
                """
            ),
            agent=agent,
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Gather In-depth City Guide Information
                    **Description**: Compile an in-depth guide for the selected city, gathering information about 
                        key attractions, local customs, special events, and daily activity recommendations. 
                        This guide should provide a thorough overview of what the city has to offer, including 
                        hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.

                    **Parameters**: 
                    - Cities: {city}
                    - Interests: {interests}
                    - Travel Date: {travel_dates}

                    **Note**: {self.__tip_section()}
                """
            ),
            expected_output = dedent(
                """
                **Expected Output**:
                - An in-depth city guide for {city} that includes:
                - **Key Attractions**: A list of must-visit landmarks, attractions, and popular activities tailored to traveler interests.
                - **Local Customs and Etiquette**: Insight into local customs, cultural norms, and etiquette tips that travelers should be aware of.
                - **Special Events**: Details on any upcoming festivals, seasonal celebrations, or unique events occurring around the travel dates.
                - **Daily Recommendations**: Suggested daily activities or tours, including a mix of well-known spots and hidden gems for a well-rounded experience.
                - **Weather Forecast**: A summary of expected weather conditions for the travel dates, including temperature ranges and notable weather patterns.
                - **Estimated Costs**: High-level cost breakdowns for typical daily expenses, covering meals, transportation, entry fees, and accommodation options.
                """
            ),
            agent=agent,
        )