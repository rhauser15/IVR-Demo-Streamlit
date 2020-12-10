import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from vardata import *
from Config import *

##Importing SID/Auth
from twilio.rest import Client


##Importing

client = Client(account_sid, auth_token)


####Streamlit User design###
st.title('Teacher Monitoring')

st.write('Substitutes needed')


st.map(map_data)


#Chart
df = pd.DataFrame({
  'Total Teachers': [100],
  'Teachers In': [satUp],
  'Teachers Out': [satDown]
})

df

le = pd.DataFrame({
    'Lead Engineers': ["Roger", "Ted", "Tyrell"],
    'Contact Numbers': [+19199498424, +19199498424, +19199498424]
})

le.set_index('Lead Engineers', inplace=True)

le

le2 = pd.DataFrame({
    'Lead Engineers': ["Roger", "Ted", "Tyrell"],
    'Contact Numbers': [+19199498424, +19199498424, +19199498424]
})

#Interactive checkbox
if st.button('Sattelite Down Test'):
    message = client.messages.create(
        to="+19199498424",
        from_="+19048228670",
        body="alert")



    print(message.sid)
    print(leEngineer + " has been noified")

    st.write('1 Satellite(s) are down. Roger has been notified')




#sidebar oganization
option = st.sidebar.selectbox(
    'Lead Engineer on-Call',
     le2['Lead Engineers'])

leEngineer = option
