import re


# INSERT  INTO `scheduler_pairs`(`id`,`donor_exchange`,`donor_symbol`,`exchange_symbol`,`min_amount`,`min_order`,`max_order`,`active`,`updated_at`,`schedule_set_id`) VALUES 
# (1,'lbank','BTC/USDT','BTC_USDT','0.000001','0.00000001','10000000000',1,'2023-10-28 18:35:43.000000',1);

file_path = './volume_settings.sql'
header = ['id','donor_symbol','exchange_symbol','min_amount','min_order','max_order','until1','until2','active']
regex = r"\((\d+),'([^']+)','([^']+)','([\d.]+)','([\d.]+)','([\d.]+)','(\d+)','([\d.]+)',(\d+)\),?"

sql_data = []


with open(file_path, 'r') as file:
    for line in file:
        matching = re.match(regex, line)
        if matching:
            value = [matching[i] for i in range(1, 10)]
            data = dict(zip(header, value))
            base, money = data['exchange_symbol'].split("_")
            data['donor_symbol'] = f"{base}/{money}"
            sql_data.append(data)

with open('migrate.sql', 'w') as file:
    for line in sql_data:
        file.write(f"('binance', '{line['donor_symbol']}', '{line['exchange_symbol']}', '{line['min_amount']}', '{line['min_order']}', '{line['max_order']}', {line['active']} ,'2023-10-28 18:35:43.000000',1), \n"  )
