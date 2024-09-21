# Web Pages Conent Listener
If the script detect web pages has chaged, send the message to Line to notify you.

## Usage
1. Fork repo
2. Set the ```main.py```:
- ```get_content()``` and notify messages.
3. Open the github action repo permission: 
- Settings -> Actions -> General -> Workflow permissions
- Check ```Read and write permissions```
- Click ```save``` to save the setting.
4. Set line notification token: 
- Settings -> Secrets and Variables -> Actions
- Click ```New repository secret```
- name is ```line_token1```, value is your line token.
5. Run script:
- Got to github action, choose ```Commit Files``` and click ```Run workflow``` run it.
- It will run **2 times every day auto automatically** by remove the annotations for ```schedule``` in ```main.yml```.
