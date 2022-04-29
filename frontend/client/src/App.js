import { useState } from 'react';
import axios from 'axios';
import './App.css';

const apiUrl = "http://localhost:5000/api/v1/get-sorted-word-frequency"
function App() {
  const [textInput, setTextInput] = useState("");
  const [result, setResult] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    // const params = {
    //   str: textInput
    // };
    
    var formdata = new FormData();
    //add three variable to form
    formdata.append("str", textInput);
    
    axios({
      method: "post",
      headers: {
        'Content-Type': 'application/json'
      },
      url: apiUrl,
      data: {
        str: textInput
      }
    })
    .then(res => {
      setResult(res.data);
    })
    .catch((err) => console.log(err));
  };

  return (
    <div className="App">
        <form onSubmit={handleSubmit}>
          <h3> Enter your amazing text! 🦄 </h3>
          <input 
            type="text"
            value={textInput}
            onChange={(e) => setTextInput(e.target.value)}
          />
          <input type="submit" />
        </form>
        <div className="word-list">
          {Object.keys(result).map((key, i) => (
            <p key={i}>
              <span>{key} </span>
              <span>{result[key]}</span>
            </p>
          ))}
        </div>
    </div>
  );
}

export default App;
