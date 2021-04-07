# Created by Ratna Sinha at 4/2/2021
Feature: Test Scenarios for Main Page functionality

  Scenario: "Latest Products on Sale" text is shown
    Given Open GetTop page
    Then text LATEST PRODUCTS ON SALE is shown

  Scenario:  Every product has Sale icon, image, product category, name, price, and star-rating
    Given Open GetTop page
    Then Verify sale icon is visible
    And Verify image is displayed
    And Verify product category is displayed
    And Verify product name is displayed
    And Verify price is displayed
    And verify star rating is displayed

  Scenario:  User can click on heart icon to add to wishlist
    Given Open GetTop page
    When Hover over and click on heart icon to add to wish list
    #And Click on heart icon to go to wish list page
    Then verify product appears in wish list page


  Scenario:User can open product from Sale and add it to cart
     Given Open GetTop page
    When Click on a product from LATEST PRODUCTS ON SALE section
    And Click on ADD TO CART
    And Click on cart icon
    Then verify item appears in cart

  Scenario:User can open product from Sale and see product price and description
    Given Open GetTop page
    When Click on a product from LATEST PRODUCTS ON SALE section
    Then Verify product price shown
    And verify product description shown

  Scenario:User can open and close Quick View by clicking on closing X
    Given Open GetTop page
    When hover over product and click on quick view
    #And Click on quick view
    Then verify quick view opens
    And verify quick view closes when X is clicked

  Scenario: User can click Quick View and add product to cart
    Given Open GetTop page
    When hover over product and click on quick view
    And Click on ADD TO CART
    Then verify item added message appears in main page

  Scenario: User can click Quick View and click through product images
    Given Open GetTop page
    When hover over product and click on quick view
    Then Click through product images

  Scenario: User sees correct categories under Browse
    Given Open GetTop page
    Then Verify Correct categories under Browse section is displayed

  Scenario:  User can click on categories under Browse and correct page opens
    Given Open GetTop page
    Then Click on categories under browse and verify correct page opens

  Scenario: No products added to the wishlist shown if no product were added to the list
    Given Open wishlist page
    Then verify No products added to the wishlist message

