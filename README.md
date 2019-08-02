# Wild Globe Explorer

<div align="center">
<img src="https://i.ibb.co/qB1yJPF/Screenshot-6.png" alt="Screenshot-6" border="0"></a>
</div>
Not that long ago I was able to see a beaver in its natural environment.
This made me thinking won't it be cool to have a website where you can have a database with all the animals you spotted in the wild.

The link to live page: [Wildlife Globe Explorer](https://wildlife-globe-explorer.herokuapp.com/)


## UX
 
#### User Stories
- As a user I want to be able to add my own animal on the site

- As a user I want to be able to have an option to delete what I submitted

- As a user I want to  be able to edit the data I submitted

- As a user I want to have a form to contact the developer of the website.

- As a user I want to be able to see all the animals I put in on the website.

#### Design

The site is easy to use and got buttons with a clear use of style and design.
On mobile devices the layout is with big buttons and big enough pictures of their animal (if added) in the spotlist.
The navigation bar got a hamburger icon that brings up a sidenav with all the links to the pages.
On tablet this hamburger icon isn't there and are the links just in the navigation bar to the right.

### Wireframes

- [Desktop Homepage](https://i.ibb.co/D4fxFw7/Desktop-Homepage-test-2.png)
- [Desktop Edit page](https://i.ibb.co/pzMQjXw/Desktop-Edit.png)
- [Mobile Homepage](https://i.ibb.co/4NhSmQy/Mobile.png)


## Features

- <u>Delete button:</u> Allow users to click the button to delete their animal they put in the spotlist
- <u>Edit button:</u> Allow users to click on the button where they can edit their animal they put in the spotlist
- <u>Accordion with pictures</u> Allow users to click on the black arrow next to the picture to have extra information pop out of their animal


### Features Left to Implement
- Having an achievement page. Where you can unlock achievement trophies
  The user can get those by completing different task. Example: Spotted 10 different animals.
-  A search function so the user can search on different classes of animals. Birds, Reptiles, Mammals



## Technologies Used

- [Materialize](https://materializecss.com/) 
    - The project uses **Materialize** as a framework.
    
- HTML
    -  standard markup language for this project.

- [AWS Cloud9](https://aws.amazon.com/cloud9/) 
    - **AWS Cloud9** used for their IDE while building and testing the website.
- CSS3
    - The project uses **CSS3** to style it.

- [GitHub](https://github.com/)
    - The project uses **GitHub** to store and share all project code to the github site.

- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) 
   - for the version control.

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) 
   - the database used to have the data in the project.

- [Imgbb](https://imgbb.com) 
   - to upload all external images.

- [Heroku](https://www.heroku.com/)
    - The application is deployed to **heroku** 

- [JQuery](https://jquery.com) 
    - DOM manipulation.

- [Flask](https://flask.palletsprojects.com/en/1.0.x/) 
    - render the pages.

- [Google Fonts](https://fonts.google.com/) 
    - for website fonts styles.


## Testing

### Manual testing: 

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer 

#### 1. Add animal on the website:

##### by clicking on the button
1. Go to the begin page with the green button that read: "Click me".
   2. Click on this button and it brings you to a page with the title: "Your spotted animal" with a form to fill in.
   3. Fill in everything on the form and click the add animal button.
   4. Now your animal got added to the list.

##### by clicking on the link in the navigation bar
 Desktop and Tablet:
1. Go to any page on the website and click on the second link "Add Spot" link.
2. This brings you to a page with the title "Your spotted animal" with a form to fill in.
3. Fill in the form and click the add animal button.
4. Now your animal got added to the list.

Mobile:
1. Click on the hamburger icon which is on the left of the title "Wildlife Globe Explorer"
2. A side navigation comes up to the left.
3. Click the second link that reads: "Add Spot"
4. This brings you to a page with the title "Your spotted animal" with a form to fill in.
5. Fill in everything on the form and click the add animal button.
6. Now your animal got added to the list.


#### 2. How to delete animal on the website:
Desktop and Tablet:
1. Click on the third link with the text: "spotlist".
2. Now you see the animal you added on the page.
3. If you not see any animal or data you put in go back to the step Add animal on the website.
4. If you do see it then you can click on the button under the animal you want to delete.
5. This is the red button with the text "Delete" on it.
6. Be Aware that once it is clicked the data is gone forever unless you re add it again.

Mobile:
1. Click on the hamburger icon which is on the left of the title "Wildlife Globe Explorer"
2. A side navigation comes up tot the left.
3. Click the third link that read: "Spotlist".
4. This brings you to a page with all the animals you added.
5. If you not see any animal or data you put in go back to "1. Add animal to the website".
6. If you do see it then you can click on the button under the animal you want to delete.
7. This is the red button with the text "Delete" on it.
8. Be Aware that once it is clicked the data is gone forever unless you re add it again.

#### 3. Edit the animal you put in the list:
Desktop and Tablet:
1. Click on the third link with the text: "spotlist".
2. Now you see the animal you added on the page.
3. If you not see any animal or data you put in go back to "1. Add animal to the website".
4. If you do see it then you can click on the button under the animal you want to delete.
5. This is the green button with the text "Edit" on it.
6. Now it brings you back to the form with your filled in content to be edited.
7. If done click on the green button with the text "Edit Animal"
8. This brings you back to the list with all your animals and you can see the edits you done.

Mobile:
1. Click on the hamburger icon which is on the left of the title "Wildlife Globe Explorer"
2. A side navigation comes up tot the left.
3. Click the third link that read: "Spotlist".
4. This brings you to a page with all the animals you added.
5. If you not see any animal or data you put in go back to "1. Add animal to the website".
6. If you do see it then you can click on the button under the animal you want to edit.
7. This is the green button with the text "Edit" on it.
8. Now it brings you back to the form with your filled in content to be edited.
9. If done click on the green button with the text "Edit Animal"
10. This brings you back to the list with all your animals and you can see the edits you done.


#### 4. Contact the developer
Desktop and Tablet:
1. Click on the fourth link with the text: "contact".
2. This brings up a form. Here you fill in your email and the message you want to be sent.
3. After done click on the green button with the text "Send Message"
4. This will send your message to the developer of the website.

Mobile:
1. Click on the hamburger icon which is on the left of the title "Wildlife Globe Explorer"
2. A side navigation comes up tot the left.
3. Click the fourth link that read: "Contact".
4. This brings up a form. Here you fill in your email and the message you want to be sent.
5. After done click on the green button with the text "Send Message" 
6. 4. This will send your message to the developer of the website.

#### 5. See all the animals on the website you entered:
Desktop and Tablet:
1. Click on the third link with the text: "spotlist".
2. Now you see all the animal you added on the page.
3. If you not see any animal or data you put in go back to "1. Add animal to the website".

Mobile:
1. Click on the hamburger icon which is on the left of the title "Wildlife Globe Explorer"
2. A side navigation comes up tot the left.
3. Click the fourth link that read: "Spotlist".
4. Now you see all the animal you added on the page.
5. If you not see any animal or data you put in go back to "1. Add animal to the website".


### Automatic test:

I used a unittest to test a GET function.
This is done by the code:  self.assertIn(b'Boar', result.data)
Where 'Boar' can be any data that is in the actual database/spotlist
If its in the database the test passed if its not it is failed.

#### Bugs
- Datepicker
  - Google Chrome:  When you are on the add animal page. And try to click on the datepicker it wont show up unless you first once clicked on the right mouse button.
    This is a bug in Materialize itself.

## Deployment
This project was developed using the [AWS Cloud9 IDE](https://aws.amazon.com/cloud9/?origin=c9io), committed to git and pushed to GitHub using the built in function within cloud9.

To deploy this project to GitHub Pages from its GitHub repository, the following steps were done:

1. Log into GitHub account.
2. From the list of repositories on the screen, select Errepulify/Repositories/wildlife-globe-explorer
3. From the menu items near the top of the page, select Settings.
4. Scroll down to the GitHub Pages section.
5. Under Source click the drop-down menu labelled None and select Master Branch
6. On selecting Master Branch the page is automatically refreshed, the repository is now ready to be deployed.
7. Scroll back down to the GitHub Pages section to retrieve the link to the deployed website.

### How to run this project locally

To clone this project from GitHub:
1. Follow this link to the [GitHub repository](https://github.com/Errepulify/wildlife-globe-explorer).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```console
git clone https://github.com/USERNAME/REPOSITORY
```
7. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://help.github.com/en/articles/cloning-a-repository).

## Heroku Deployment

To deploy Wildlife Globe Explorer to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

10. The site is now successfully deployed.


## Media

- The picture used as background is from [shutterstock](https://www.shutterstock.com/nl/image-vector/amazon-jungle-trees-wilderness-92162701)

## Code

- collapsible code is from [Materialize](https://materializecss.com/collapsible.html) 
- testing code is from [Unittest](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)
- the emailJS code is from Code institute.

### Acknowledgements

- I received inspiration for this project from pokemon.
- My mentor Juan Monetti who helped and explained me alot.
- Special thanks to the tutor team of Code Institute to answer all my questions I had during this milestone project.
- The webinairs of students in the Slack channel

