import React, {useEffect} from 'react';
import axios from 'axios';
const App = (props) => {
    useEffect(() => {
        const apiCall = async () => {
            const response = await axios.get('http://127.0.0.1:8000/api/');
            console.log(response.data);
        };
        apiCall();
    }, [])
    return (<div></div>);
};
export default App;
