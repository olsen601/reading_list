# reading_list
A Django web app to organize a users reading list based on user defined genres i.e. 'work', 'school', etc.

This is meant to be used with the reading_api repo.

  Database

    First:
          Create a Postgresql database called readinglist.
          Create a user with acess to the readinglist database called reader.
          (set a password for the reader and give read/write access)

    Second:
          Set the following environment variables.
              DATABASE=readinglist
              USER=reader
              PASSWORD=<password>
              HOST=localhost

  Django

    First:
          Create a virtual environment outside of the repository.
          Activate the virtual environment and move to back to the repository.

    Second:
          Install the requirements using pip.
            <pip install -r requirements.txt>

    Third:
          Migrate the model into the database.
            <python manage.py makemigrations>
            <python manage.py migrate>

    Four:
          Populate data into the database with the reading_api repository.

              Part A:
                    Generate a Google API key in the Google Developer Console.
              Part B:
                    Set an environment variable of GB_KEY to the value of the Google API Key.
              Part C:
                    Change directories into the reading_api/request and use the following command.
                      <python test_call.py>
                      <python test_call_two.py>
                    Change directories to the parent directory.
              Part D:
                    Insert the initial data into the database using the following commands.
                      <python main.py>
                      <python alternative.py>

    Five:
          Navigate back to the reading_list repository and run the following command.
            <python manage.py runserver>
          Next open a web browser and enter '127.0.0.1:8000/' the loopback address on port 8000.

          If all goes well your page should look like the following image.
          ![Alt text](https://github.com/olsen601/reading_list/blob/master/screenShots/Capture1.PNG?raw=true)

    Walk-through:
          Click on the "Login or Create Account" hyperlink.
          Now you should see the following screen.
          ![Alt text](https://github.com/olsen601/reading_list/blob/master/screenShots/Capture2.PNG?raw=true)

          Click the "Create an Account" hyperlink.
          Now you should see the following screen.
          ![Alt text](https://github.com/olsen601/reading_list/blob/master/screenShots/Capture3.PNG?raw=true)
          Fill in the required fields to create an account.
          After submission you will be automatically redirected to the home page and automatically logged in.
          ![Alt text](https://github.com/olsen601/reading_list/blob/master/screenShots/Capture4.PNG?raw=true)
