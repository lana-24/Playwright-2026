# PRACTICE SOFTWARE TESTING (toolshop)
simple automation software toolshop testing 

## Tools
- **Python** 3.12.12
- **Playwright** 
- **Pytest**

## Development Environment
- **Emacs**
- **Ubuntu os [via gh codespace]**

## What can this code do?
- login test
- chekcout test
- filter test

## How to run?
1. **Clone** this repo.
2. **Open** folder `/toolshop`.
3. **Install** requirements: `pip install playwright pytest python-dotenv`
4. **Install** browsers: `playwright install chromium`
5. **Rename** `.env.example` to `.env`.
6. **Edit** `.env` with your credentials:
   - EMAIL: customer3@practicesoftwaretesting.com
   - PASSWORD: pass123
7. **Run** tests: `pytest`


## Test Case

| ID    | Feature | Test Scenarios                                             | Expected Result                                 |
|-------|---------|------------------------------------------------------------|-------------------------------------------------|
| TC-01 | Login   | login with valid email and password                        | login success                                   |
| TC-02 | Login   | login with invalid email                                   | login failed, show massage invalid email        |
| TC-03 | Login   | login with invalid password                                | login failed, show massage invalid password     |
| TC-04 | Login   | login with empty email                                     | login failed, show message invalid credentials  |
| TC-05 | Login   | login with empty password                                  | login failed, show message invalid credentials  |
| TC-06 | Login   | login with empty email and password                        | login failed, show message invalid credentials  |
| TC-07 | Logout  | logout after success login                                 | logout success and back to login page           |
| TC-08 | Sort    | sort products by name A-Z                                  | product names starting with A will appear first |
| TC-09 | Sort    | sort products by name Z-A                                  | product names starting with Z will appear first |
| TC-10 | Sort    | sort products by price High-Low                            | product with higher price will appear first     |
| TC-11 | Sort    | sort products by price Low-High                            | product with lower price will appear first      |
| TC-12 | Search  | search product with valid credential and product available | product will show available                     |
| TC-13 | Search  | search product with product unavailable                    | product won't show available                    |
| TC-14 | Search  | search product with invalid special symbols                | product won't show available                    |
| TC-15 | Search  | search product with empty credentials                      | nothing happen                                  |
