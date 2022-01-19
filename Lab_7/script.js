
const defult_weather={  // дефолтные параметры погоды
  q: "Москва",
  lang: "ru",
  units: "metric",
  mode: "json",
  appid: "c787af9e580ad611dbafdd74c14cf98e",
};

const keyApi = 'c787af9e580ad611dbafdd74c14cf98e';
const strFetch = new URL(`https://api.openweathermap.org/data/2.5/weather?q=${defult_weather.q}&appid=${defult_weather.appid}&lang=${defult_weather.lang}&units=${defult_weather.units}`);
const strForecast = new URL(
  `https://api.openweathermap.org/data/2.5/forecast?q=${defult_weather.q}&lang=${defult_weather.lang}&units=${defult_weather.units}&appid=${defult_weather.appid}`);
const contentDom = document.querySelector('.content');
//https://api.openweathermap.org/data/2.5/weather?q=Москва&units=metric&lang=ru&appid=c787af9e580ad611dbafdd74c14cf98e' 
//`https://api.openweathermap.org/data/2.5/forecast?q=Москва&lang=ru&mode=json&units=metric&appid=c787af9e580ad611dbafdd74c14cf98e`

//--------------------- работа с кнопкой
function change(weth_url, fc_url) {  // меняем значения погоды
  let city_val1 = document.getElementById("input_city").value;
  if (city_val1 == "" || city_val1 == undefined){
    city_val1 = defult_weather.q;
  }
  weth_url.searchParams.delete("q");
  weth_url.searchParams.append("q", city_val1);
  fc_url.searchParams.delete("q");
  fc_url.searchParams.append("q", city_val1);


  fetch(weth_url) //   получение данных о погоде
  .then(res => res.json())
  .then(res => {
    PutWeather(res);
  });

  fetch(fc_url) //   получение данных о прогнозе
  .then(res => res.json())
  .then(res => {
    console.log(res);
    PutForecast(res);
  });
};

let button = document.getElementById("search_button");
button.addEventListener("click", () => change(strFetch, strForecast));  // нажатие на кнопку
document.addEventListener("DOMContentLoaded", () =>change(strFetch, strForecast))

//---------------------- запись данных
function PutWeather(json) {
  var now = new Date();
  // Вывод города
  document.getElementById("city").innerHTML = json.name;
  // Вывод даты
  document.getElementById("date").innerHTML = CorrectDay(now.getDay()) + " " + now.getDate() + "." + CorrectMonth(now.getMonth())+ " " + now.getHours() + ":" + now.getMinutes()
      + ":" + now.getSeconds();
   // Вывод температуры
   document.getElementById("temperature").innerHTML = CorrectTemp(json.main.temp) + " ℃";
   // Вывод давления
    document.getElementById("pressure").innerHTML = "Давление: " + Math.round(json.main.pressure / 1.3) + " мм рт.ст.";
   // Вывод влажности
   document.getElementById("humidity").innerHTML = "Влажность: " + json.main.humidity + " %";
   // Вывод скорости ветра
   document.getElementById("wind").innerHTML = "Ветер: " + json.wind.speed + " м/с";
  // Вывод картиночки погоды
   document.getElementById("weather_pic").innerHTML = `<img src="https://openweathermap.org/img/wn/${json.weather[0].icon}@2x.png"} />`;
   // Вывод описания погоды
   document.getElementById("condition").innerHTML = `${json.weather[0].description}`;
};

function CorrectTemp(temp){
  return temp > 0 ? `+${Math.round(temp)}` : `${Math.round(temp)}`;
};

function CorrectDay(day){
  switch (day) {
    case 0:
      return "воскресенье";
    break;
    case 1:
      return "понедельник";
    break;
    case 2:
      return "вторник";
    break;
    case 3:
      return "среда";
    break;
    case 4:
      return "четверг";
    break;
    case 5:
      return "пятница";
    break;
    case 6:
      return "суббота";
    break;
  }
};

function CorrectMonth(month){
  if (month < 10) {
    return "0" + month +1;
  }
  return 1+month;
};

function PutForecast(json) {
  document.getElementById("fc__tomorrow").innerHTML = "Tomorrow";
    // Вывод даты
    document.getElementById("fc1__date").innerHTML = json.list[7].dt_txt;
    // Вывод картиночки погоды
    document.getElementById("fc1__weather_pic").innerHTML = `<img src="https://openweathermap.org/img/wn/${json.list[7].weather[0].icon}@2x.png"} />`;
    // Вывод температуры
    document.getElementById("fc1__temperature").innerHTML = `${CorrectTemp(json.list[7].main.temp)}` + " ℃";
    // Вывод описания погоды
    document.getElementById("fc1__condition").innerHTML = `${json.list[7].weather[0].description}`;
    // Вывод давления
    document.getElementById("fc1__pressure").innerHTML = "Давление: " + Math.round(json.list[7].main.pressure / 1.3) + " мм рт.ст.";
    // Вывод скорости ветра
    document.getElementById("fc1__wind").innerHTML = "Ветер: " + json.list[7].wind.speed + " м/с";
    // Вывод влажности
    document.getElementById("fc1__humidity").innerHTML = "Влажность: " + json.list[7].main.humidity + " %";

     document.getElementById("fc2__date").innerHTML = json.list[9].dt_txt;
     document.getElementById("fc2__weather_pic").innerHTML = `<img src="https://openweathermap.org/img/wn/${json.list[9].weather[0].icon}@2x.png"} />`;
     document.getElementById("fc2__temperature").innerHTML = `${CorrectTemp(json.list[9].main.temp)}` + " ℃";
     document.getElementById("fc2__condition").innerHTML = `${json.list[9].weather[0].description}`;
     document.getElementById("fc2__pressure").innerHTML = "Давление: " + Math.round(json.list[9].main.pressure / 1.3) + " мм рт.ст.";
     document.getElementById("fc2__wind").innerHTML = "Ветер: " + json.list[9].wind.speed + " м/с";
     document.getElementById("fc2__humidity").innerHTML = "Влажность: " + json.list[9].main.humidity + " %";
  
}