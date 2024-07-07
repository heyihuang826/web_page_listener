# Web Pages Conent Listener
## Explain
If the script detect ```web pages has chaged```, send the message to Line to ```notify you```.
## Usage
1. Set the main.py:
- ```get_content()``` and notify messages.
2. Open the github action repo permission: 
- Settings -> Actions -> General -> Workflow permissions
- Check ```Read and write permissions```
- Save the setting.
3. Set line notification token: 
- Settings -> Secrets and Variables -> Actions
- Click ```New repository secret```
- name is ```line_token1```, value is your line token.
4. got to github action, choose "Commit Files" and run it, or it will run 2 times every day auto automatically in default.