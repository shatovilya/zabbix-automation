import settings
import json
from pyzabbix import ZabbixAPI

def main():
    disable_unsupported_items()
    group = settings.group
    update_tags(group)


def disable_unsupported_items():
    
    print("Run disable unsupported items")
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
    print(f"Disable Unsupported data {len(unsupported_item)}")


def update_tags(group_name):
    
    print("Run update tags")
    zapi = ZabbixAPI(settings.ZabbixAPI_URL)
    zapi.login(settings.Zabbix_Login, password=settings.Zabbix_Password)

    host_item = 0
    id_group_name_get = zapi.hostgroup.get(filter={"name": group_name})
    
    id_group_name = json.loads(id_group_name_get[0].get('groupid'))
    
    host_get = zapi.host.get(
        groupids=id_group_name, output=['hostid', 'name'])
    counter = 0

    
    Services = settings.Services_tag
    alert    = settings.alert_tag
    Location = settings.Location_tag
    
    print(f"Services: {Services}")
    print(f"alert: {alert}")
    print(f"Location: {Location}")
    print(f"Group name: {group_name}")
    print(f"Count update hosts: {len(host_get)}")
    
    answer = input("Enter yes or no: ") 
    if answer == "yes":
        while counter < len(host_get):
            host_item = json.loads(host_get[counter].get('hostid'))
            counter += 1
            zapi.do_request(
                'host.update',
                {
                    "hostid": host_item,
                    "tags": [
                        {
                            "tag": "Services",
                            "value": Services
                        },
                        {
                            "tag": "alert",
                            "value": alert
                        },
                        {
                            "tag": "Location",
                            "value": Location
                        }
                    ]
                }
            )
        print(f"Count update hosts: {len(host_get)}")    
    elif answer == "no": 
        print("Exit")

if __name__ == '__main__':
    main()
