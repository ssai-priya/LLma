import { Button, DialogActions, Divider, Typography,Select,MenuItem, Input } from "@mui/material";
import './gitpushmodal.css'
import { useState, useEffect } from 'react';



export default function NewBranchModal(props){
    const [name,setName] = useState('');
    const [branch,setBranch] = useState('');
    
    const handleBranchNameChange = (event) => {
        setName(event.target.value);
    };
    const handleBranchChange = (event) => {
        setBranch(event.target.value);
    }; 

    return(
        <div className="modal-box h-full">
            <div className="title-text mb-4 mt-4">
            <Typography className="title-text">Create New Branch</Typography>
            </div>
            <Divider className="divider"></Divider>
            
            <div className="input-box mt-4 mb-4">
                <Typography className="input-box-text">
                Enter New Branch Name
                </Typography>
                <Input value={name} onChange={handleBranchNameChange}></Input>
            </div>
            <Divider className="divider"></Divider>
            <div className="input-box mt-4 mb-4">
                <Typography className="input-box-text">
                Select Start Branch
                </Typography>
                <Select className='select' value={branch} onChange={handleBranchChange}>
                    <MenuItem value={1}>Main</MenuItem>
                    <MenuItem value={2}>Rep 1</MenuItem>
                    <MenuItem value={3}>Rep 2</MenuItem>
                </Select>
            </div>
            <Divider className="divider"></Divider>
            <DialogActions className="buttons">
                <Button className="cancel" onClick={props.handleCloseBranchModal} >
                    Cancel
                </Button>
                <Button variant="contained" className="push">
                    Create
                </Button>
            </DialogActions>
        </div>
    )
}