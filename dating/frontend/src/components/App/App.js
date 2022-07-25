import React, {Component} from "react"
import {render} from "react-dom";

function App() {

    return (
    <div>
        <h1>Dev done</h1>
        <div>
            frontend start dev
        </div>
    </div>
    )
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv)