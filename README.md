# Installation
pip install -i https://test.pypi.org/simple/ rapicio

# Usage 
```
>>> from rapicio.rapicClient import Rapic
>>> rapic_client = Rapic("username","password")
>>> rapic_client.login()
>>> my_data = rapic_client.get_data("project_name","object_name")
>>> rapic_client.post_data("project_name","object_name", {"data": "value"})
>>> rapic_client.update_data("project_name","object_name", myDataID, {"data": "newValue"})
>>> rapic_client.delete_data("project_name","object_name", myDataID)
```
