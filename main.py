import json
from pyzabbix import ZabbixAPI

import settings

zapi = ZabbixAPI(settings.ZabbixAPI_URL)
zapi.login(settings.Zabbix_Login, password=settings.Zabbix_Password)


found_unsupported_item = zapi.item.get(filter={"state": 1, "status": 0})


print(f"Found unsupported data {len(found_unsupported_item)}")
counter = 0
while counter < len(found_unsupported_item):
    itemid = json.loads(found_unsupported_item[counter].get('itemid'))
    print(itemid)
    counter += 1
    zapi.do_request(
        'item.update',
        {
            "itemid": itemid,
            "status": "1",
        }
    )

unsupported_item = zapi.item.get(filter={"state": 1, "status": 0})
print("Unsupported data", len(unsupported_item))
