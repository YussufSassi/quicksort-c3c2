class TableManager
{
	constructor()
	{
		this.sortDirectionBtn = document.getElementById('sort-direction');
		this.sortDirectionBtn.addEventListener('change', (event) =>
		{
			this.fetchData(event.target.value);
		});
		this.fetchData('asc');
	}

	fillTable(bugDataArr)
	{
		let tableBody = document.querySelector('#table-body');
		tableBody.innerHTML = '';
		for(let i = 0; i < bugDataArr.length; i++)
		{
			let row = tableBody.insertRow(i);
			row.insertCell(0).innerHTML = String(i + 1);
			row.insertCell(1).innerHTML = bugDataArr[i].id;
			row.insertCell(2).innerHTML = (new Date (bugDataArr[i].date * 1000)).toLocaleDateString();

			if(bugDataArr[i].status === 0)
			{
				row.insertCell(3).innerHTML = 'Neu';
			}
			else if(bugDataArr[i].status === 1)
			{
				row.insertCell(3).innerHTML = 'In Bearbeitung';
			}
			else
			{
				row.insertCell(3).innerHTML = 'Gelöst';
			}

			if(bugDataArr[i].priority === 0)
			{
				row.insertCell(4).innerHTML = 'Mittel';
			}
			else if(bugDataArr[i].status === 1)
			{
				row.insertCell(4).innerHTML = 'Hoch';
			}
			else
			{
				row.insertCell(4).innerHTML = 'Sehr Hoch';
			}
			row.insertCell(5).innerHTML = bugDataArr[i].description;
			row.insertCell(6).innerHTML = bugDataArr[i].affected_users;
		}
	}

	async fetchData(sortDirection)
	{
		try
		{
			const response = await fetch(`http://localhost:5000/sort?dir=${sortDirection}`);
			const data = await response.json();
			this.fillTable(data.data);
		}
		catch(error)
		{
			console.error('Error:', error);
		}
	}
}

new TableManager();