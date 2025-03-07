import React from 'react';
import './Card.css';

const Card = ({ className, children }) => {
    return (
        <div className={`${className} card`}>
            {children}
        </div>
    );
};

export default Card;