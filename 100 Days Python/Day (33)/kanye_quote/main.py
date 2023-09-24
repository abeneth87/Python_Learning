from tkinter import *
import requests

def get_quote():
    try:
        # Make a GET request to the Kanye West quote API
        response = requests.get("https://api.kanye.rest/")

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Parse the JSON response to obtain the quote text
        quote_data = response.json()
        quote = quote_data["quote"]

        # Update the text on the canvas
        canvas.itemconfig(quote_text, text=quote)

    except requests.exceptions.RequestException as e:
        # Handle any request-related exceptions (e.g., connection error)
        print("Error:", e)
    except KeyError:
        # Handle the case where the API response doesn't contain the expected data
        print("Error: Unable to parse quote data")



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()