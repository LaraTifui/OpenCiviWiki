# Report for Assignment 1 resit

## Project chosen

Name: CiviWiki

URL: https://github.com/LaraTifui/OpenCiviWiki

Number of lines of code and the tool used to count it: 4958 line (using lizard)

Programming language: Python

## Coverage measurement with existing tool

Tool used:  Coverage.py

Execution:  

            coverage run --branch -m pytest // for the test
            
            coverage report // to see the report
            
            coverage html // to see the report as well as the code covered, in html form
            
Initial run of the tool (in terminal):

![init cov report part1](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/3b6590e9-f4ee-4ce2-a2a2-5224fd22d421)
![init cov report part2](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/44856e3e-8fea-4ecb-8e0d-1b8ae7efbeb2)

## Coverage improvement

### Individual tests


  ### *Function 1*

In project/accounts/tests/test_models.py I have added a test that checks if the profile has a set profile image.
The function profile_image_url,  had 50% branch test coverage, since a unit test already existed in the case a profile had no image associated with it, so the default image is used. After adding 1 unit tests , in order to check if the profile is correctly set when an image is associated with the profile,  the function has now 100% branch coverage and the total coverage of the models.py file has raised from  57% to 86%

Code:
![image](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/533f5056-5908-4026-bc5c-57e470ed16f6)


The commit link for the new test for function 1:
https://github.com/LaraTifui/OpenCiviWiki/commit/1fa0f9baf80d0e7188b4991ccb1915d41e389588#diff-6ca9982ebb8b28073aa65d5339359b92b701121f06ac0ba9b3606b81c83bdc69


Old coverage result:
![func1 init uncovered 1](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/bc6a96c3-f246-49e6-bd9b-192ea084acc7)

New coverage result:
![func1 final covered ](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/1eace442-3b86-4a25-89a2-042dc7633b1b)

Old coverage:
![func1 init stat](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/014822e0-eca9-4542-95c5-987083736c8a)

New coverage:

![func1 final stat](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/56e3c672-f1a4-481c-9c96-7c5891a2667e)




### *Function 2*
In project/accounts/tests/test_utils.py there is a function called get_account to which I created a test for.
The function get_account, which has 3 optional parameters,  had 0% test coverage. After adding 5 unit tests , in order to check each of the possible calling situations covered by the function coding, the function has now 100% branch coverage and the total coverage of the utils.py file has raised from  32% to 65%.


The commit link for the new test for function 1:
https://github.com/LaraTifui/OpenCiviWiki/commit/3c1d9fb5b823a0cbf4a2b359affa05db09de8bf7


Old coverage result:

![func2 init uncovered get_account](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/eb27c587-27b3-489d-93f1-dfecc0da07fb)


New coverage result:

![func2 final covered ](https://github.com/user-attachments/assets/66b9b766-ca86-40d4-bfc8-d36717a74d3c)


Old coverage:

![func2 init stat](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/da4934bc-ef24-4828-87e3-e39b247b5183)


New coverage:

![func2 final stat](https://github.com/user-attachments/assets/33a6aa22-0f14-4e5b-bf7e-e2a8b63c34de)



### Overall

Initial run of the tool (in html form):

![init index cov part1](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/96cf04fd-f255-44b7-81d7-4e1086d1eb2c)
![init index cov part2](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/ccd7f057-71aa-420b-97b3-b521589f0f7d)


Final run of the tool (in html form):

![fin index cov part1](https://github.com/user-attachments/assets/8f3e2ab1-fd3f-4ad6-a17e-48960597af4b)
![fin index cov part2](https://github.com/user-attachments/assets/5ebea506-3cd6-4299-a216-5477e2ad2ac9)

