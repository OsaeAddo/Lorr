import React from "react";
// import { motion } from "framer-motion"
// import { FaBeer } from 'react-icons/fa';



import { Navbar, Footer, Products, BottomBar } from "../components/all-components";


const Home = () => {

    return (
        <div className='min-h-screen'>
            <div className=''>
                <Navbar />
                {/* <FaBeer /> */}
            </div>

            <div>
                <Products />
            </div>

            <div>
                <BottomBar />
            </div>

            <div>
                <Footer />
            </div>

        </div>
    )
}


export default Home;