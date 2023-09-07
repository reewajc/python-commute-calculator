from datetime import datetime, timedelta
import googlemaps
from twilio.rest import Client

def main():
        duration = get_commute_duration()
        now = datetime.now()
        arrival_time = (now - duration).strftime("%I:%M:%S %p")

        message = (
            f"Good morning!\n"
            f"Estimated comute time from home to work at 8:30 am: {duration} \n"
            f"Leave now for work at 8am to arrive at approximately {arrival_time}"
        )
        print(message)

        send_text_message(message)

def send_text_message(message):
        twillio_account_id = "<account_id>"
        twillio_account_token = "<token>"     
        twillio_phone_bumber = "+15555555555"
        your_phone_number = "+16666666666"  
        
        client = Client(twillio_account_id, twillio_account_token)
        message = client.messages.create(
            body=message,
            from_=twillio_phone_bumber,
            to=your_phone_number
            )


def get_commute_duration():
        home_address = "55 Coding Ave"
        work_address = "66 Working Ave"

        google_map_api_key = "<api_key>"
        gmaps = googlemaps.Client(key=google_map_api_key)
        directions = gmaps.directions(home_address, work_address)
        first_leg = directions[0]['legs'][0]
        duration = first_leg['duration']['text']
        delta = timedelta(minutes=int(duration.split()[0]))
        return delta
      

if __name__ == "__main__":
        main()


    