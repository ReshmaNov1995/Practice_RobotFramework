*** Settings ***
Library  Seleniumlibrary

*** Variables ***
${browser}  chrome  #variablename  valueofthevariable
${url}  https://demo.nopcommerce.com/

*** Test Cases ***
LoginTest #Testcase name
  create webdriver  chrome  executable_path = "mention driver path" # Not required while the driver is involved in the project
  open browser  ${url}  ${browser}
  LoginToApplication
  close browser
  
*** Keywords ***
# Userdefined Keywords can be created and utilised in Testcase section
LoginToApplication  #keyword name
  click link  xpath://a[@class='ico-login'] # while it's a link("a" tag)
  input text  id:Email  reshu123@gmail.com
  input text  name:Password  12345
  click element  linktext:Log in  # Try it

HTML Report is available in venv folder
