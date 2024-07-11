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
The test also checks if the image is set but also if it isn't set.

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

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced tests for function 1>

<Provide a screenshot of the old coverage results for such function>

<Provide a screenshot of the new coverage results for such function>

<State the coverage improvement with a number and elaborate on why the coverage is improved>


### Overall

Initial run of the tool (in html form):

![init index cov part1](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/96cf04fd-f255-44b7-81d7-4e1086d1eb2c)
![init index cov part2](https://github.com/LaraTifui/OpenCiviWiki/assets/121812597/ccd7f057-71aa-420b-97b3-b521589f0f7d)



<Provide a screenshot of the new coverage results by running the existing tool using all test modifications>
