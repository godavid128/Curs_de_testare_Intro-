
# BDD = e defapt o practica de dezvoltare a softurilor prin care aduci in mai aproape partea non-tehnica de cea tehnic
  # Ele ajung sa fie teste, si chiar teste automate, prin scrierea cuvint in engleza, care respecta o anumit structura
# GHERKIN SYNTAX:
# implica 3 Pasi: 1.Feature, 2.Scenario, 3. Folosind 5 cuv cheie: Gi en, When, Them, And, But

Feature: Login to the internet
    As a user
    I want to login on this site
    So that I can entre in my account

    Scenario: test invalid login
      Given I have an invalid user
      And an invalid password
      When I send them to the login form
      Then wrong text message will be displayed on the screen

    Scenario: test invalid login
      Given I have an valid user
      And an invalid password
      When I send them to the login form
      Then wrong text message will be displayed on the screen