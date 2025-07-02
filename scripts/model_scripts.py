
import pickle
import pandas 


def load_model():
    ## import model
    model = pickle.load(open('./model/model_9451.pkl', 'rb'))
    return model 



class FitnessMeasure:

    def __init__(self):
        self.model = load_model()


    def predict(self, total_steps: int, very_active_minutes: float, calories: int) -> int:
        ## collecting user data
        data: dict = {
            'TotalSteps': total_steps,
            'VeryActiveMinutes': very_active_minutes,
            'Calories': calories
        }

        ## converting as pandas dataframe
        df = pandas.DataFrame(data=data, index=[0])

        prediction = self.model.predict(df)[0]

        return int(prediction)



if __name__ == "__main__":

    model = FitnessMeasure()
    prediction = model.predict(total_steps=8000, very_active_minutes=23, calories=1200)
    print(prediction)



