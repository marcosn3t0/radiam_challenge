Feature: Flights Reservation
    3 most crucial flows:
        1 - Verify that users can search for flights by name, 
        from-to airports or flight code for checking their status and timings
        2 - Verify one way and Round trip options 
        3 - choose diferent travellers age and number of travellers
        4 - choose diferent airplane classes
        5 - verify searching datas after to search flights

    Scenario Outline: One-way Multiple Flight's search
        Given I go to PHPTRAVELS

        When I select one way trip
        And I fill the country I am going out <flying_from> 
        And I fill the country I am going to <flying_to> 
        And I fill the date I am going to travel <depart_date>
        And I click on search button

        Then I verify found flights

        Examples:
        |flying_from                        |flying_to              |depart_date        |
        |DXB                                |New Orleans            |01-12-2023         |
        |Alama Iqbal International Airport  |Brasil                 |01-12-2023         |

    Scenario Outline: Round-trip Flight's search
        Given I go to PHPTRAVELS

        When I select one way trip
        And I fill the country I am going out <flying_from> 
        And I fill the country I am going to <flying_to> 
        And I fill the date I am going to travel <depart_date>
        And I fill the date I am going back <return_date>
        And I click on search button

        Then I verify found flights

        Examples:
        |flying_from                        |flying_to              |depart_date    |return_date|
        |DXB                                |BER                    |01-12-2023     |05-12-2023 |
        |BER                                |DXB                    |10-12-2023     |05-12-2023 |
        |BER                                |DXB                    |10-12-2022     |05-12-2023 |

    Scenario: Inform travellers and number of travellers
        Given I go to PHPTRAVELS

        When I select round trip
        And I fill the country I am going out <flying_from> 
        And I fill the country I am going to <flying_to> 
        And I fill the date I am going to travel <depart_date>
        And I select travellers age Adults and number of travellers 2
        And I click on search button

        Then I verify found flights

    Scenario Outline: inform multiple travellers with distint ages
        Given I go to PHPTRAVELS

        When I select round trip
        And I fill the country I am going out <flying_from> 
        And I fill the country I am going to <flying_to> 
        And I fill the date I am going to travel <depart_date>
        And I select travellers age <traveller_age> and number of travellers <traveller_number>
        And I select travellers age <traveller_age> and number of travellers <traveller_number>
        And I select travellers age <traveller_age> and number of travellers <traveller_number>
        And I click on search button

        Then I verify found flights

        Examples:
        |flying_from                        |flying_to              |depart_date    |traveller_age  |traveller_number   |
        |DXB                                |BER                    |01-12-2023     |Adults         |2                  |
        |BER                                |DXB                    |10-12-2023     |Childs         |2                  |
        |BER                                |DXB                    |10-12-2022     |Infants        |9                  |


        Scenario Outline: One-way Multiple Flight's search
        Given I go to PHPTRAVELS

        When I select one way trip
        And I fill the country I am going out <flying_from> 
        And I fill the country I am going to <flying_to> 
        And I fill the date I am going to travel <depart_date>
        And I select Airplane classes <airplane_classes>
        And I click on search button

        Then I verify found flights

        Examples:
        |flying_from                        |flying_to              |depart_date    |airplane_classes   |
        |DXB                                |New Orleans            |01-12-2023     |Economy            |
        |BER                                |DXB                    |10-12-2022     |Economy Premium    |
        |BER                                |DXB                    |10-12-2022     |Business           |    
        |BER                                |DXB                    |10-12-2022     |First              |
