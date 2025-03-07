import React from 'react';
import './Chat.css';
import clsx from "clsx";

const Chat = ({isUser = false, text}) => {

    return (
        <>
            {isUser ? (
                <div className="flex justify-end mr-5 ">
                    <div className="w-[60%] flex justify-end">
                        <div className="user__text whitespace-normal mr-5 p-5">{text}</div>
                        <img className={`h-12 w-12 rounded-full`}
                             src="https://thumbs.dreamstime.com/b/rainbow-love-heart-background-red-wood-60045149.jpg"
                             alt=""/>
                    </div>
                </div>
            ) : (
                <div className="flex justify-start ml-5">


                    <div className="w-[60%] flex">
                        <img className={`h-12 w-12 rounded-full`}
                             src="https://thumbs.dreamstime.com/b/rainbow-love-heart-background-red-wood-60045149.jpg"
                             alt=""/>
                        <div className="comm__text whitespace-normal ml-5 p-5">{text}</div>

                    </div>
                </div>
            )}


        </>


    )
        ;
};

export default Chat;