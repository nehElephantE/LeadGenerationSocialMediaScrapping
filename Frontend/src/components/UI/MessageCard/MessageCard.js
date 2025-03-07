import React from 'react';
import './MessageCard.css';
import { Chat } from 'react-chat-popup';

const MessageCard = () => {
    const handleUserMessage = (newMessage) =>{
        console.log(`New message incoming~ ${newMessage}`);
        // send msg to backend
    }

    return (
        <div>
            <Chat handleNewUserMessage = {this.handleNewUserMessage}/>
        </div>
    );
};

export default MessageCard;