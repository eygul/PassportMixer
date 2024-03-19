import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
with open('passport_data.json', 'r') as f:
    data = json.load(f)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    countries = [
        ["AL", "Albania"],
        ["DZ", "Algeria"],
        ["AD", "Andorra"],
        ["AO", "Angola"],
        ["AG", "Antigua and Barbuda"],
        ["AR", "Argentina"],
        ["AM", "Armenia"],
        ["AU", "Australia"],
        ["AT", "Austria"],
        ["AZ", "Azerbaijan"],
        ["BS", "Bahamas"],
        ["BH", "Bahrain"],
        ["BD", "Bangladesh"],
        ["BB", "Barbados"],
        ["BY", "Belarus"],
        ["BE", "Belgium"],
        ["BZ", "Belize"],
        ["BJ", "Benin"],
        ["BT", "Bhutan"],
        ["BO", "Bolivia"],
        ["BA", "Bosnia and Herzegovina"],
        ["BW", "Botswana"],
        ["BR", "Brazil"],
        ["BN", "Brunei Darussalam"],
        ["BG", "Bulgaria"],
        ["BF", "Burkina Faso"],
        ["BI", "Burundi"],
        ["KH", "Cambodia"],
        ["CM", "Cameroon"],
        ["CA", "Canada"],
        ["CV", "Cape Verde"],
        ["CF", "Central African Republic"],
        ["TD", "Chad"],
        ["CL", "Chile"],
        ["CN", "China"],
        ["CO", "Colombia"],
        ["KM", "Comoros"],
        ["CG", "Congo"],
        ["CD", "Congo, Democratic Republic of the"],
        ["CR", "Costa Rica"],
        ["CI", "Cote d'Ivoire"],
        ["HR", "Croatia"],
        ["CU", "Cuba"],
        ["CY", "Cyprus"],
        ["CZ", "Czech Republic"],
        ["DK", "Denmark"],
        ["DJ", "Djibouti"],
        ["DM", "Dominica"],
        ["DO", "Dominican Republic"],
        ["EC", "Ecuador"],
        ["EG", "Egypt"],
        ["SV", "El Salvador"],
        ["GQ", "Equatorial Guinea"],
        ["ER", "Eritrea"],
        ["EE", "Estonia"],
        ["SZ", "Eswatini"],
        ["ET", "Ethiopia"],
        ["FJ", "Fiji"],
        ["FI", "Finland"],
        ["FR", "France"],
        ["GA", "Gabon"],
        ["GM", "Gambia"],
        ["GE", "Georgia"],
        ["DE", "Germany"],
        ["GH", "Ghana"],
        ["GR", "Greece"],
        ["GD", "Grenada"],
        ["GT", "Guatemala"],
        ["GN", "Guinea"],
        ["GW", "Guinea-Bissau"],
        ["GY", "Guyana"],
        ["HT", "Haiti"],
        ["HN", "Honduras"],
        ["HK", "Hong Kong"],
        ["HU", "Hungary"],
        ["IS", "Iceland"],
        ["IN", "India"],
        ["ID", "Indonesia"],
        ["IR", "Iran, Islamic Republic of"],
        ["IQ", "Iraq"],
        ["IE", "Ireland"],
        ["IL", "Israel"],
        ["IT", "Italy"],
        ["JM", "Jamaica"],
        ["JP", "Japan"],
        ["JO", "Jordan"],
        ["KZ", "Kazakhstan"],
        ["KE", "Kenya"],
        ["KI", "Kiribati"],
        ["XK", "Kosovo"],
        ["KW", "Kuwait"],
        ["KG", "Kyrgyzstan"],
        ["LA", "Lao People's Democratic Republic"],
        ["LV", "Latvia"],
        ["LB", "Lebanon"],
        ["LS", "Lesotho"],
        ["LR", "Liberia"],
        ["LY", "Libya"],
        ["LI", "Liechtenstein"],
        ["LT", "Lithuania"],
        ["LU", "Luxembourg"],
        ["MO", "Macao"],
        ["MG", "Madagascar"],
        ["MW", "Malawi"],
        ["MY", "Malaysia"],
        ["MV", "Maldives"],
        ["ML", "Mali"],
        ["MT", "Malta"],
        ["MH", "Marshall Islands"],
        ["MR", "Mauritania"],
        ["MU", "Mauritius"],
        ["MX", "Mexico"],
        ["FM", "Micronesia, Federated States of"],
        ["MD", "Moldova, Republic of"],
        ["MC", "Monaco"],
        ["MN", "Mongolia"],
        ["ME", "Montenegro"],
        ["MA", "Morocco"],
        ["MZ", "Mozambique"],
        ["MM", "Myanmar"],
        ["NA", "Namibia"],
        ["NR", "Nauru"],
        ["NP", "Nepal"],
        ["NL", "Netherlands"],
        ["NZ", "New Zealand"],
        ["NI", "Nicaragua"],
        ["NE", "Niger"],
        ["NG", "Nigeria"],
        ["KP", "North Korea"],
        ["MK", "North Macedonia"],
        ["NO", "Norway"],
        ["OM", "Oman"],
        ["PK", "Pakistan"],
        ["PW", "Palau"],
        ["PS", "Palestine, State of"],
        ["PA", "Panama"],
        ["PG", "Papua New Guinea"],
        ["PY", "Paraguay"],
        ["PE", "Peru"],
        ["PH", "Philippines"],
        ["PL", "Poland"],
        ["PT", "Portugal"],
        ["QA", "Qatar"],
        ["RO", "Romania"],
        ["RU", "Russian Federation"],
        ["RW", "Rwanda"],
        ["KN", "Saint Kitts and Nevis"],
        ["LC", "Saint Lucia"],
        ["WS", "Samoa"],
        ["SM", "San Marino"],
        ["ST", "Sao Tome and Principe"],
        ["SA", "Saudi Arabia"],
        ["SN", "Senegal"],
        ["RS", "Serbia"],
        ["SC", "Seychelles"],
        ["SL", "Sierra Leone"],
        ["SG", "Singapore"],
        ["SK", "Slovakia"],
        ["SI", "Slovenia"],
        ["SB", "Solomon Islands"],
        ["SO", "Somalia"],
        ["ZA", "South Africa"],
        ["KR", "South Korea"],
        ["SS", "South Sudan"],
        ["ES", "Spain"],
        ["LK", "Sri Lanka"],
        ["VC", "St. Vincent and the Grenadines"],
        ["SD", "Sudan"],
        ["SR", "Suriname"],
        ["SE", "Sweden"],
        ["CH", "Switzerland"],
        ["SY", "Syrian Arab Republic"],
        ["TW", "Taiwan"],
        ["TJ", "Tajikistan"],
        ["TZ", "Tanzania, United Republic of"],
        ["TH", "Thailand"],
        ["TL", "Timor-Leste"],
        ["TG", "Togo"],
        ["TO", "Tonga"],
        ["TT", "Trinidad and Tobago"],
        ["TN", "Tunisia"],
        ["TR", "Turkey"],
        ["TM", "Turkmenistan"],
        ["TV", "Tuvalu"],
        ["UG", "Uganda"],
        ["UA", "Ukraine"],
        ["AE", "United Arab Emirates"],
        ["GB", "United Kingdom"],
        ["US", "United States"],
        ["UY", "Uruguay"],
        ["UZ", "Uzbekistan"],
        ["VU", "Vanuatu"],
        ["VA", "Vatican City"],
        ["VE", "Venezuela"],
        ["VN", "Vietnam"],
        ["YE", "Yemen"],
        ["ZM", "Zambia"],
        ["ZW", "Zimbabwe"],
        ["AF", "Afghanistan"]
    ]
    visafree = 0
    visarequired = 0
    search_item = request.form.get('search')
    search_item1 = request.form.get('search1')
    for item in data:
        if item == search_item:
            dataitem = data[item]
            listitem = [[key, value] for key, value in dataitem.items()]
            for item in listitem:
                if item[1]== 1:
                    item[1] = 'green'
                    #visafree +=1
                else:
                    item[1] = 'red'
                    #visarequired +=1
            print(listitem)
            for country in countries:
                if country[0]== search_item:
                    full_country = country[1]
                if search_item1 != "":
                    if country[0] == search_item1:
                        full_country1 = country[1]
                else:
                    full_country1 = ""
    for item1 in data:
        if search_item1 != "":
            if item1 == search_item1:
                dataitem1 = data[item1]
                listitem1 = [[key, value] for key, value in dataitem1.items()]
                for item1 in listitem1:
                    if item1[1]== 1:
                        item1[1] = 'green'
                        #visafree +=1
                    else:
                        item1[1] = 'red'
                        #visarequired +=1
                print(listitem1)
        else:
            listitem1 = listitem
    for element in range (len(listitem)):
        if listitem1[element][1]== 'green':
            listitem[element][1] = 'green'
    print(listitem)
    for item in listitem:
        if item[1] == 'green':
            visafree +=1
        else:
            visarequired +=1
    world_reach = (visafree/len(listitem)*100)
    return render_template("map.html", listitem= listitem, search_item=full_country, visafree=visafree, visarequired=visarequired, full_country1=full_country1, world_reach=world_reach)

if __name__ == '__main__':
    app.run(port=3000)