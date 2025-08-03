# 读取cvs数据
# 读取cvs数据
import csv

input_csv_file = r'E:\GitHub\0101\Vul\SSH\2766622bba_202504251025资产数据.csv'
output_txt_file = r'E:\GitHub\0101\Vul\SSH\hosts.txt'
host_column_name = 'host' # 假设包含主机信息的列名为 'host'，如果不是请修改

print(f"Reading hosts from: {input_csv_file}")
print(f"Saving hosts to: {output_txt_file}")

hosts = []
try:
    with open(input_csv_file, mode='r', newline='', encoding='utf-8-sig') as infile: # 使用 utf-8-sig 以处理可能的 BOM
        reader = csv.DictReader(infile)
        if host_column_name not in reader.fieldnames:
            print(f"Error: Column '{host_column_name}' not found in the CSV file.")
            print(f"Available columns: {reader.fieldnames}")
            exit(1)

        for row in reader:
            host = row[host_column_name].strip()
            if host: # 确保主机名不为空
                hosts.append(host)

except FileNotFoundError:
    print(f"Error: Input file not found at {input_csv_file}")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading the CSV file: {e}")
    exit(1)

try:
    with open(output_txt_file, mode='w', encoding='utf-8') as outfile:
        for host in hosts:
            outfile.write(host + '\n')
    print(f"Successfully extracted {len(hosts)} hosts and saved to {output_txt_file}")

except Exception as e:
    print(f"An error occurred while writing to the output file: {e}")
    exit(1)