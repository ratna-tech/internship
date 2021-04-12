# Created by Ratna Sinha at 4/6/2021
Feature: Products page features
  # Enter feature description here

   Scenario: Sort by Average Rating
    Given open all products page
    When  sort products by average rating
    Then 1st product has rating stars displayed after sorting
    And User can click through product pages after sorting is done

   Scenario:  User can open and close Quick view and click through pages
     Given open all products page
     Then User can open and close Quick View by clicking on closing X
     And User can click Quick View and add product to cart
     And User can click trough multiple product pages by clicking 1, 2 for page number
     And User can click trough multiple product pages by clicking > and <