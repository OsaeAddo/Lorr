import React from "react";
// import { motion } from "framer-motion"
// import { FaBeer } from 'react-icons/fa';



import { Navbar, Footer, Items } from "../components/all-components";


const Home = () => {

    return (
        <div className='min-h-screen'>
            <div className=''>
                <Navbar />
                {/* <FaBeer /> */}
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