import { useState } from 'react';
import axios from 'axios';
import './App.css';

const apiUrl = "http://localhost:5000/api/v1/get-sorted-word-frequency"
function App() {
  const [textInput, setTextInput] = useState("");
  const [result, setResult] = useState([]);
  const [errorMessage, setErrorMessage] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

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
      setErrorMessage("")
    })
    .catch((err) => {
      console.log(err.response.data);
      setErrorMessage(err.response.data);
      setResult([]);
    });
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
          {result && Object.keys(result).map((key, i) => (
            <p key={i}>
              <span>{key} </span>
              <span>{result[key]}</span>
            </p>
          ))}
        </div>
        {errorMessage && <p className='error-message'>{errorMessage}</p>}
    </div>
  );
}

export default App;
