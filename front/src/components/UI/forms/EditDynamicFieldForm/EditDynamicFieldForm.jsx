import React from 'react';
import { Card } from '@mui/material';
import CardContent from '@mui/material/CardContent';
import { CardActions } from '@mui/material';
import Typography from '@mui/material/Typography';
import { Link, Button } from '@mui/material';
import {TextField} from '@mui/material';
function EditDynamicFieldForm(props) {
    const SubmitButton = (props) => (<button {...props} type='submit' />);

    return (

        <Card variant="outlined">
            <CardContent style={{ paddingBottom: '1em' }}>
                <br />
                <Typography variant="h6">Заявка на изменение поля "{props.data.field}"</Typography>
                <br />
                <form className="container">

                    <div className="row"> <TextField required id="standard-basic" label="Введите вашу редакцию" variant="standard" /></div>
                    <div className="row"> <TextField id="standard-basic" label="Введите комментарий" variant="standard" /></div>
                    <br />
                    <CardActions>
                        <Button size="small" component={SubmitButton} variant='contained' color='success'>Отправить</Button>
                        <Button size="small" variant='contained' color='error'>Отменить</Button>
                    </CardActions>
                    </form>
            </CardContent>
        </Card>

    );
}

export default EditDynamicFieldForm;