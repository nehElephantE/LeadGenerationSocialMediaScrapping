import React, {useState} from 'react';
import Card from "../UI/Card/Card";
import Button from "../UI/Button/Button";
import './SignUp.css'
import axios from 'axios';
import {useNavigate} from "react-router-dom";

const SignUp = () => {
    const navigate = useNavigate();
    const [userdetails, setUserDetails] = useState({
        "first_name": "",
        "last_name": "",
        "email": "",
        "twitter": "",
        "password": "",
    })

    function handleSubmit(){
        fetch("http://localhost:8000/api/newUser/",
        {
            method: "POST",
            body:JSON.stringify({
                ...userdetails,
            "interests": [
                "finance", "loans"
            ]
        })
        }).then(res=>console.log(res.status)).then(()=>navigate("/options"))
    }

    return (
        <>
            <div className="signup-page">
                <div className="flex w-screen h-screen justify-between items-center">
                    <div className="mx-auto login-page__img flex justify-center text-center">
                        <img className="w-[80vh] text-center" src={require("../Assets/signup.png")} alt=""/>

                    </div>
                    <div className="flex-col">
                        <div className="flex flex-col w-[100vh] px-[15%] signup__box text-center ">


                                <h1 className="signup-heading">MetaData</h1>


                                <span className="block text-left font-[iceland] signup-text">Signup</span>
                                <hr className="my-3 w-[25%] border-2 border-black"/>
                                <p className="text-left font-[Montserrat] font-[300] text-[20px]">Welcome onboard with
                                    us!</p>
                                <form className="flex-col gap-[40px] justify-between mt-10">
                                    <p className="text-left font-[Montserrat] mt-3 mb-2 font-[400]">firstname</p>
                                    <input
                                        className="signup__input text-left px-4 py-1 w-full text-[20px] placeholder:font-[Montserrat] font-[500] font-[15px] focus:outline-none"
                                        placeholder="Enter your username"
                                            value={userdetails.first_name}
                                            onChange={(e)=>setUserDetails({
                                                ...userdetails,
                                                [e.target.name]: e.target.value
                                            })}
                                        type="text"
                                        name="first_name"/>
                                    <p className="text-left font-[Montserrat] mt-3 mb-2 font-[400]">lastname</p>
                                    <input
                                        className="signup__input text-left px-4 py-1 w-full text-[20px] placeholder:font-[Montserrat] font-[500] font-[15px] focus:outline-none"
                                        placeholder="Enter your username"
                                        value={userdetails.last_name}
                                        onChange={(e)=>setUserDetails({
                                            ...userdetails,
                                            [e.target.name]: e.target.value
                                        })}
                                        type="text"
                                        name="last_name"/>
                                    <p className="text-left font-[Montserrat] mt-3 mb-2 font-[400]">Email</p>
                                    <input
                                        className="signup__input text-left px-4 py-1 w-full text-[20px] placeholder:font-[Montserrat] font-[500] font-[15px] focus:outline-none"
                                        placeholder="Enter your email"
                                        value={userdetails.email}
                                        onChange={(e)=>setUserDetails({
                                            ...userdetails,
                                            [e.target.name]: e.target.value
                                        })}
                                        type="email"
                                        name="email"/>
                                    <p className="text-left font-[Montserrat] mt-3 mb-2 font-[400]">Twitter</p>
                                    <input
                                        className="signup__input text-left px-4 py-1 w-full text-[20px] placeholder:font-[Montserrat] font-[500] font-[15px] focus:outline-none"
                                        placeholder="Enter your username"
                                        value={userdetails.twitter}
                                            onChange={(e)=>setUserDetails({
                                                ...userdetails,
                                                [e.target.name]: e.target.value
                                            })}
                                        type="text"
                                        name="twitter"/>
                                    <p className="text-left font-[Montserrat] mt-3 mb-2 font-[400]">Password</p>
                                    <input
                                        className="signup__input text-left px-4 py-2 w-full text-[20px] placeholder:font-[Montserrat] font-[500] font-[15px] focus:outline-none"
                                        placeholder="Enter your username"
                                        value={userdetails.password}
                                        onChange={(e)=>setUserDetails({
                                            ...userdetails,
                                            [e.target.name]: e.target.value
                                        })}
                                        type="password"
                                        name="password"/>

                                    <Button onClick={handleSubmit} className="w-full my-10">Signup</Button>
                                </form>

                        </div>

                    </div>

                </div>

            </div>
        </>
    );
};

export default SignUp;