/**
 * Input form, contains textarea ind a button
 * @packageDocumentation
 */
import React, { useState } from 'react';
import { Box, Grid, Button, TextField } from '@material-ui/core';
import { withStyles } from '@material-ui/core';

const styles = {
  inputform: {
    width: '40vw',
    height: '100%',
    margin: '5vh 5vw',
  },
  button: {
    width: '100%',
    maxHeight: '60px',
  },
  textInput: {
    width: '100%',
    height: '80vh',
    '& div': {
      width: '100%',
      height: '100%',
      display: 'flex',
      alignItems: 'flex-start',
      '& textarea': {
        lineHeight: '20px',
        fontSize: '16px',
        overflow: 'auto',
        resize: 'none',
      },
      '& fieldset': {
        width: '100%',
        height: '100%',
      },
    },
  },
};

/** InputForm */
export default withStyles(styles)((props: any) => {
  const [text, setText] = useState('');
  const { classes } = props;
  // Determines textarea max size
  const height = window.screen.height;
  const lineHeight = 20;
  const rows = Math.floor((height * 0.75) / lineHeight);
  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    alert(text);
    event.preventDefault();
  }
  return (
    <form onSubmit={handleSubmit} className={classes.inputform}>
      <TextField
        label="Insert your text here"
        className={classes.textInput}
        variant="outlined"
        multiline
        rowsMax={rows}
        value={text}
        onInput={(event: any) => setText(event.target.value)}
      />
      <Box display="flex" width="100%" justifyContent="flex-end">
        <Grid xs={8} md={6} lg={4}>
          <Button type="submit" variant="contained" color="primary" className={classes.button}>
            Submit
          </Button>
        </Grid>
      </Box>
    </form>
  );
});
