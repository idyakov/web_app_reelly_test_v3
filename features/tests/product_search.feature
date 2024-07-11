Feature: Test Scenarios for Search functionality of soft.reelly page
  Scenario:
    Given Open soft.reelly page_
    And Login to the page_
    And Click on continue button
    And Click on settings open__
    And Click on Edit profile option_
    And Enter some test information in the input fields_
    And Check the right information is present in the input fields
    And Click on Save changes_
    Then Click on Close_
#@verify
#  Scenario: User sign on main page functionality
#    Given Open soft.reelly page
#    When Input name field
#    Then Input phone field
#    And Input pwd field
#    And Input comp_web field
#    And Choose role field
#    And Choose country field
#    And Choose comp_size field
#    And Verify expected URL
#@smoke
#  Scenario: User login main page and verify switch page functionality
#    Given Open soft.reelly page
#    And Login to the page_
#    And Click on continue button
#    And Store original window
#    And Click on “Connect the company”
#    And Switch to new window
#    And Verify the right tab opens
#    And Close the current page and switch back
#
#@drink



