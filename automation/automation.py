
import re

with open('assets/potential-contacts.txt','r')as f:

    data=f.read()

def get_email(data):
    
    
    match_email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', data)
    sorted_match_email=sorted(set(match_email))
    join_email='\n'.join(sorted_match_email)

    with open('assets/emails.txt','w')as f:
        f.write(join_email)

def get_phone( data ):

    match_phone_number = re.findall( r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', data )
    
    all_phone_number = []

    for phone in match_phone_number:
        
        if "(" in phone:
            phone = phone.replace( "(", "" )
        if ")" in phone or "." in phone:
            phone = phone.replace( ")", "-" )
            phone = phone.replace( ".", "-" )
        if len( phone ) == 10:
            phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
        if not phone in all_phone_number:
            all_phone_number.append( phone )
    all_phone_number = sorted( all_phone_number )


    with open( 'assets/phone_numbers.txt', 'w' ) as result:
        for phone in all_phone_number:
            result.write( f"{phone}\n" )

if __name__ == "__main__":
    email = get_email(data)
    phone_number = get_phone(data)
# jd

