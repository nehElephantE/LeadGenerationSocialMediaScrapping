import React from 'react';
import './Header.css';
import { Link } from 'react-router-dom';
import {AdjustmentsIcon, MenuAlt3Icon} from "@heroicons/react/outline";
import {useAuthState} from "react-firebase-hooks/auth";
import {auth, provider} from "../../firebase";
import {useNavigate} from "react-router-dom";

import {signInWithPopup} from 'firebase/auth';
import Button from "../UI/Button/Button";

const Header = (props) => {
    const [user] = useAuthState(auth);
    const navigate = useNavigate();

    const signIn = (e) => {
        e.preventDefault();
        signInWithPopup(auth, provider)
            .then((result) => {
                navigate('/homepage')
                // const credential = GoogleAuthProvider.credentialFromResult(result);
                // const token = credential.accessToken;
                // const user = result.user;
            }).catch((error) => alert(error.message));
    };

    return (

        <header className="flex bg-[#DCF9FD] items-center justify-between py-4 px-6 mb-1 w-screen sticky">
            <a href="/">
                <img
                    src={require("../Assets/MetaData.png")}
                    className="w-32 h-12 object-contain"
                    alt="Hello"
                />
            </a>
            <div className="hidden flex lg:flex space-x-6">
                <a href="/" className="navbar__link">Home</a>
                <a href="/community" className="navbar__link">Community</a>

            </div>

            <div className="flex space-x-4">

                <Button><Link to="/dashboard">Dashboard</Link></Button>
                <Link to="/profile"><img className="h-10 w-10 profile__img rounded-full"
                                        src="https://thumbs.dreamstime.com/b/rainbow-love-heart-background-red-wood-60045149.jpg"
                                        alt=""/>
                </Link>
                <MenuAlt3Icon className="h-9 text-[#741188] cursor-pointer lg:hidden"/>

            </div>
        </header>
    );
};

export default Header;