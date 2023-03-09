# files that go through here have to named Cimpress_ and matched as a first check

from order.read_xml_write_json import xml_in_json_out, ready_for_mapping_
from pathlib import Path

from order.ordervila_esko_order_information_os import Job, Customer

dwd_F_xml = Path(r'../order/data_xml/F6HADBE637/Cimpress_F6HADBE637.xml')

dwd_job = ready_for_mapping_(xml_in_json_out(dwd_F_xml))

# remapping 1

prod_man = dwd_job['orderMetadata']['items']['item']['productManufacturingData']
items_item = dwd_job['orderMetadata']['items']['item']

width = str(int(prod_man['Custom-Width']) * 10)
height = str(int(prod_man['Custom-Height']) * 10)
size = width + ' x ' + height + " mm"

drukwerkdeal_job_mapped = Job(OrderId=dwd_job['orderMetadata']['orderId'],
                              SubOrderId=dwd_job['orderMetadata']['merchantId'],  # staat nu als prepress?
                              OrderYear=dwd_job['orderMetadata']['promisedArrivalDate'][0:4],
                              Name=items_item['name'],
                              Description=items_item['description'],
                              DueDate=dwd_job['orderMetadata']['promisedArrivalDate'],
                              JobStatus='always approved',
                              ProjectId=dwd_job['orderMetadata']['merchantOrderId'],

                              Category="-",
                              Proof='always approved',
                              Dispenser='False',  # property in jobs

                              LabelDirection=dwd_job['orderMetadata'],
                              Adhesive=prod_man['Adhesion-Stickers'],

                              Size=size,
                              JobFolder=dwd_job['orderMetadata'],
                              JobType=prod_man['Printing-Process'],
                              Handling='0',
                              QOrder='0', )

drukwerkdeal_customer_mapped = Customer(CustomerId='105696',
                                        CustomerName='DRUKWERKDEAL.NL',
                                        CustomerDescription=dwd_job['orderMetadata']['orderId'],
                                        CustomerJobReference='',
                                        JobHandler='automatic',
                                        JobHandlerEmail='prepress@vila.nl',
                                        )
n