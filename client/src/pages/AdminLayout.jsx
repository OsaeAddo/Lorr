import React from "react";
import { Outlet } from "react-router-dom";

import {Navbar} from "../components/all-components"

const AdminLayout = () => {
    return (
        <>
            <Navbar />
            <Outlet />
        </>
    )
}

export default AdminLayout;