import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)

count = 0
for item in data['imdata']:
    if count >= 3:
        break
        
    attributes = item['l1PhysIf']['attributes']
    
    dn = attributes['dn']
    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')
    
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")
    count += 1
