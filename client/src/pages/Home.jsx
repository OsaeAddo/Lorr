import React from "react";
import { Navbar, Footer, Items } from "../components/all-components";


const Home = () => {

    return (
    <div className='min-h-screen'>
        <div className=''>
            <Navbar />
        </div>

        <div>
            <Items />
        </div>

        <div>
            <Footer />
        </div>

    </div>)
}


export default Home;