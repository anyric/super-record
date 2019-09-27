from datetime import datetime
from easy_pdf.views import PDFTemplateView

today = datetime.now()
company_name = "SUPERRECORD MANAGEMENT SYSTEM"
address = "P.O.Box xxx, Kampala"
tel = "+2567xxxxxxxx"

def generate_report(context, dataset, title):
    context['data'] = dataset
    company = {"name": company_name, "address": address, "tel": tel, "date": today, "title": title}
    titles = []
    for data in dataset[0].keys():
        if '_' in data:
            data = data.split('_')[0] + ' ' + data.split('_')[1]
            titles.append(data.upper())
        else:
            titles.append(data.upper())
    context['titles'] = titles
    context['company'] = company

    return context

