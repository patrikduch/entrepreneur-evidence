from xml.etree import ElementTree
from xml.etree.ElementTree import fromstring, ElementTree

class AresFetcherHelper:

	def is_ico_valid(ico):

		import json
		import requests

		xml = """<Ares_dotazy xmlns="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.1" xmlns:dtt="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_datatypes/v_1.0.1" xmlns:udt="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/uvis_datatypes/v_1.0.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" dotaz_datum_cas="2011-06-16T10:04:01" dotaz_pocet="3" dotaz_typ="Standard" vystup_format="XML" validation_XSLT="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.0/ares_request.xsl" user_mail="Vas_funkcni.e-mail@vase_firma.cz" answerNamespaceRequired="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_answer/v_1.0.1" xsi:schemaLocation="http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.1 http://wwwinfo.mfcr.cz/ares/xml_doc/schemas/ares/ares_request/v_1.0.1/ares_request_v_1.0.1.xsd" Id="ares_dotaz">
		<Dotaz>
		<Typ_vyhledani>FREE</Typ_vyhledani>
		<Klicove_polozky>
		<ICO>""" + ico + """</ICO>
		</Klicove_polozky>
		<Max_pocet>10</Max_pocet>
		</Dotaz>    
		</Ares_dotazy>"""

		headers = {'Content-Type': 'application/xml'} # set what your server accepts
		
		#test = requests.post('https://wwwinfo.mfcr.cz/cgi-bin/ares/xar.cgi', data=xml, headers=headers).text

		response = requests.post('https://wwwinfo.mfcr.cz/cgi-bin/ares/xar.cgi', data=xml.encode('utf-8'), headers=headers).text

		tree = ElementTree(fromstring(response))
		root = tree.getroot()


		found = [element for element in root.getiterator() if element.text == ico]
		is_valid = False


		for i in found:
			if i != None:
				is_valid = True

		return is_valid