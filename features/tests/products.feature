# Created by Ratna Sinha at 4/6/2021
Feature: Products page features
  # Enter feature description here

   Scenario: Sort by Average Rating
    Given open order by rating page
    When  sort products by average rating
    Then 1st product has rating stars displayed after sorting
    And User can click through product pages after sorting is done