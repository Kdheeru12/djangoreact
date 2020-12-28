import React from 'react'
import { NavLink } from 'react-router-dom';
import Link from '@material-ui/core/Link';
import Button from '@material-ui/core/Button';

export const Header = () => {
    return (
        <div className='Hello'>
            Header
            <Button
                href="#"
                color="primary"
                variant="outlined"

                component={NavLink}
                to="/logout"
            >
                Logout
					</Button>
        </div>
    )
}
