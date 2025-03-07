import React from "react";
import './Login.css'
import Card from "../UI/Card/Card";
import Button from "../UI/Button/Button";

const Login = () => {
    return (
        <>
            <div className="login-page">
                <div className="flex w-screen h-screen justify-around items-center">
                    <div className="flex-col">
                        <Card className="w-[80vh] py-10 px-[15%] text-center">


                            <h1 className="login-heading">MetaData</h1>


                            <span className="block text-left font-[iceland] login-text">Login</span>
                            <hr className="my-3 w-[25%] border-2 border-black"/>
                            <p className="text-left font-[Montserrat] font-[300] text-[20px]">Welcome back!</p>
                            <form className="flex-col gap-[40px] justify-between mt-10">
                                <p className="text-left font-[Montserrat] mb-2 font-[400]">Username</p>
                                <input
                                    className="login__input text-left px-4 py-2 w-full text-[20px] placeholder:font-[Montserrat] font-[500] font-[15px] focus:outline-none"
                                    placeholder="Enter your username"
                                    type="text"
                                    name="username"/>
                                <p className="text-left font-[Montserrat] mt-4 mb-2 font-[400]">Password</p>
                                <input
                                    className="login__input text-left px-4 py-2 w-full text-[20px] placeholder:font-[Montserrat] font-[500] font-[15px] focus:outline-none"
                                    placeholder="Enter your username"
                                    type="password"
                                    name="password"/>
                                <p className="font-[Montserrat] font-[400] text-right text-[12px] m-4">Forgot
                                    Password?</p>
                                <Button className="w-full">Login</Button>
                                <p className="font-[Montserrat] font-[300] text-[15px] m-4">New to MetaData? <span
                                    className="font-[700]">Register</span> here</p>
                            </form>


                        </Card>

                    </div>
                    <div className="login-page__img">
                        <img className="w-[80vh]" src={require("../Assets/img.png")} alt=""/>

                    </div>
                </div>

            </div>
        </>

    );
};

export default Login;
